import pdfkit
from flask import make_response, url_for
from datetime import datetime, timedelta
import os

def _create_pdf(content):
    '''
    PDFを出力する

    Parameters
    -----
    content["create_date"] : datetime.datetime
      記録の作成日

    content["start_date"] : datetime.datetime
      記録の開始日

    content["name"] : str
      作成者名

    content["journal"] : str
      週間ジャーナル総括（所感・来週までの感想）

    content["week_journal"] : [str]
      週間ジャーナル（各日）．日付の開始日はcontent["start_date"]に依存する．
    '''

    # pdfkit configuration
    config = pdfkit.configuration(wkhtmltopdf=os.getenv("PATH_TO_WKHTMLTOPDF", "/usr/local/bin/wkhtmltopdf"))

    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': "UTF-8",
        'no-outline': None,
        'dpi': '72'
    }

    fontPath = "/app/.fonts/hirakakuW6.ttc" if os.path.exists("/app/.fonts/hirakakuW6.ttc") else os.path.join(os.getcwd(), ".fonts/hirakakuW6.ttc")

    # html setting
    html = '''
    <html lang="ja">
    <head>
        <meta charset="utf-8"/>
        <title>週間ジャーナル</title>
    </head>
    <body>
    '''

    # font setting
    html += f'''
    <style>
        @font-face{{
            font-family:'hirakakuW6';
            src: url({ fontPath }) format('truetype');
        }}

        * {{
            font-family: 'hirakakuW6', sans-serif;
        }}
    '''
    
    # style setting
    html += '''
        html,body{
            height:297mm;
            width:210mm;
        }
        
        .container{
          height: 297mm;
          width: 210mm;
          padding: 5px;
        }
        .under-line{
          width:190mm;
          border-bottom: solid 5px #cc3;
          border-radius: 2px;
          margin-top: 30px;
          margin-left: 20px;
          padding-left: 30px;
          padding-bottom: 5px;
        }
        .headding{
          font-size: 2em;
          width: 80%;
        }
        .right{
          margin-top: 3px;
          margin-right: 20px;
          float: right;
          line-height: 18px;
          text-align: right;
        }
        .li-left{
          width:30mm;
          float: left;
        }
        .light{
          font-weight: lighter;
        }
        h1{
          margin-left: 15px;
          margin-top: 40px;
        }
        li{
          font-weight: bold;
          list-style: none;
          padding: 10px 0px 10px 10px;
          margin-right: 30px;
          display: flex;
          border-bottom: solid 1px #ddd;
          align-items: center;
        }
        li:nth-child(even){
          background: #eee;
        }
        p{
          margin-left: 45px;
          margin-right: 30px;
        }
    </style>
    <div class="container">
        <header class="under-line">
            <span class="headding">週間ジャーナル</span>
            <span class="right light">'''
    html += '作成日：' + str(content["create_date"].year) +'年' + str(content["create_date"].month)+'月' + str(content["create_date"].day) +'日'  + '<br/>作成者：' + content["name"]
    html += '''
    </span></header>
    '''
    
    # main journal
    html += '''
        <main>
        <h1>・ジャーナル</h1><ul>
    '''

    weekdayDict = ["月","火","水","木","金","土","日"]
    for day in range(0,7):
        tmp_day = content["start_date"] + timedelta(days=day)
        html += '<li><div class="li-left">' + str(tmp_day.month) + '/' + str(tmp_day.day) + '（' + weekdayDict[ tmp_day.weekday() ] + '）</div><div>' + content["week_journal"][day] + '</div></li>'

    html += '</ul><h1>・所感, 次週に向けての感想</h1><p>' + content["journal"] + '</p></main></div></body></html>'

    response = make_response( pdfkit.from_string(html, False, options=options, configuration=config) )
    response.headers['Content-Disposition'] = 'attachment; filename="example.pdf"'
    response.mimetype = 'application/pdf'

    return response
