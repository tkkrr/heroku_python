const getDateString = (date) => {
    if(date){ 
        return date.getFullYear() + "-" + paddingZero(date.getMonth()+1) + "-" + paddingZero(date.getDate())
    }else{
        return new Date().getFullYear() + "-" + paddingZero(new Date().getMonth()+1) + "-" + paddingZero(new Date().getDate())
    }
}

const getWeekString = (date) => {
    if(date){ 
        return (date.getMonth()+1) + "/" + date.getDate() + getWeekChar( date.getDay() )
    }else{
        return (new Date().getMonth()+1) + "/" + new Date().getDate() + getWeekChar(new Date().getDay())
    }
}

const getWeekChar = (num) => {
    switch (num){
    case 0: return "（日）";
    case 1: return "（月）";
    case 2: return "（火）";
    case 3: return "（水）";
    case 4: return "（木）";
    case 5: return "（金）";
    case 6: return "（土）";
    default: return "（）";
    }
}

const paddingZero = (num, padding=2) => {
    if(num < 0) return ""
    let strnum = String(num)
    while( strnum.length < padding ){
        strnum = "0" + strnum
    }
    return strnum
}

const getDeltaDate = (date, delta) => { 
    let deltaDate = new Date(date)
    deltaDate.setDate(date.getDate() + delta)
    return deltaDate
}

export default {
    getDateString,
    getWeekString,
    getWeekChar,
    paddingZero,
    getDeltaDate
}