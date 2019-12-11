<script>
import List from "./list"

export default {
    components: {List},
    data() { 
      return {
        start_date: new Date()
      }
    },
    filters: {
      getDateString: (date) => { return getDateString(date) },
      getWeekString: (date) => { return getWeekString(date) },
      weekName: (num) => { return "week" + num }
    },
    methods: {
      getDeltaDate(date, delta) { return getDeltaDate(date, delta) },
      handleInputChange() {
        this.start_date = new Date( document.querySelector("input[name='start_date']").value )
      }
    }
}

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

</script>





<template>
  <div class="top">
    <form action="/api/add" method="post" class="left_side">
      <table>
        <tr>
          <td><label for="name">名前</label></td>
          <td><input type="text" name="name" placeholder="筑波 太郎"/></td>
        </tr> 
        <tr>
          <td><label for="start_date">記録開始日</label></td>
          <td><input type="date" name="start_date" v-bind:value="start_date | getDateString" @change="handleInputChange" /></td>
        </tr>

        <tr v-for="n of 7" :key="n">
            <td><label for="week_journal">{{ getDeltaDate(start_date, n-1) | getWeekString }}</label></td>
            <td><input type="text" v-bind:name="n | weekName" placeholder="e.g., 研究, 就活, バイト"/></td>
        </tr>

        <tr>
          <td colspan="2" style="width:100%">
            <textarea name="journal" placeholder="所感, 次週に向けての感想"/>
          </td>
        </tr>
      </table>
      <input type="submit" name="submit" value="ジャーナルを登録" />
    </form>
    <List class="right_side"/>
  </div>
</template>





<style lang="scss" scoped>
.top {
  display: flex;
  flex-direction: row;
  margin: 0 auto;
  height: calc(100vh - 120px);
}

.left_side {
  color: white;
  background: #77868C;
  width: 30vw;
  padding: 32px;
  table {
    width: 100%;
    margin: 0 auto;
    tr {
      display: flex;
      margin-bottom: 8px;
      td {
        display: block;
        width: 70%;
        &:first-child { width: 30% }
      }
    }
  }
  label {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  input {
    width: 100%;
    padding: 6px 8px;
    border: none;
    border-bottom: 1px #aaa solid;
    background: transparent;
    color: white;
    line-height: 1.2;
    outline: none;
    box-sizing: border-box;
    transition: border-bottom 0.3s, background 0.3s, color 0.3s;
    &::placeholder {
      color: #aaa;
      line-height: 1.2;
    }
    &:focus {
      border-bottom: 1px solid white;
    }
    &[type="submit"]{
      width: auto;
      display: block;
      border: 1px solid white;
      border-radius: 4px;
      padding: 8px 24px;
      margin: 16px auto;
      &:hover{
        background: white;
        color: #77868C;
      }
    }
  }
  textarea {
    border: none;
    height: 7em;
    margin-top: 16px;
    width: 100%;
    resize: none;
    padding: 4px;
    line-height: 1.2;
    box-sizing: border-box;
    &::placeholder {
      line-height: 1.2;
    }
  }
}

.right_side {
  width: 60vw;
}
</style>