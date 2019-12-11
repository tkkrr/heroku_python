<script>
import Counter from "./counter"

export default {
    components: {Counter},
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
  <div>
    <!-- <counter/> -->

    <form action="/api/add" method="post">
      <table>
        <tr>
          <td><label for="name">名前</label>：</td>
          <td><input type="text" name="name" /></td>
        </tr> 
        <tr>
          <td><label for="start_date">記録開始日</label>：</td>
          <td><input type="date" name="start_date" v-bind:value="start_date | getDateString" @change="handleInputChange" /></td>
        </tr>

        <tr v-for="n of 7" :key="n">
            <td><label for="week_journal">{{ getDeltaDate(start_date, n-1) | getWeekString }}</label>：</td>
            <td><input type="text" v-bind:name="n | weekName" /></td>
        </tr>

        <tr>
          <td colspan="2">
            <textarea name="journal" />
          </td>
        </tr>
      </table>
      <input type="submit" name="submit" />
    </form>
  </div>
</template>





<style lang="scss">
p {
    font-size: 24px;
}
</style>