<script>
import List from "./list"
import utils from "./utils/date_to_string"

export default {
    components: {List},
    data() { 
        return {
            start_date: new Date()
        }
    },
    filters: {
        getDateString: (date) => { return utils.getDateString(date) },
        getWeekString: (date) => { return utils.getWeekString(date) },
        weekName: (num) => { return "week" + num }
    },
    methods: {
        getDeltaDate(date, delta) { return utils.getDeltaDate(date, delta) },
        handleInputChange(e) {
            const start_date = new Date( e.target.value )
            if( start_date.toString() ==  "Invalid Date") this.start_date = new Date()
            else this.start_date = start_date
        },
        handleSubmit(e) {
            const form = e.target
            fetch( form.action, {
                method: "post",
                headers: { "accept": "application/json" },
                body: new FormData(form),
                credentials: "same-origin"
            })
                .then(response => {
                    if (response.ok) form.reset()
                    else throw response
                }).catch(err => {
                    form.reset()
                    console.log(err)
                    throw err
                })
            this.$refs.list.getList()
        }
    },
}

</script>





<template>
    <div class="top">
        <form action="/api/add" method="post" class="left_side" @submit.prevent="handleSubmit">
            <table>
                <tr>
                    <td><label for="name">名前</label></td>
                    <td><input type="text" name="name" placeholder="筑波 太郎" required/></td>
                </tr> 
                <tr>
                    <td><label for="start_date">記録開始日</label></td>
                    <td><input type="date" name="start_date" v-bind:value="start_date | getDateString" @change="handleInputChange" required/></td>
                </tr>

                <tr v-for="n of 7" :key="n">
                    <td><label v-bind:for="n | weekName">{{ getDeltaDate(start_date, n-1) | getWeekString }}</label></td>
                    <td><input type="text" v-bind:name="n | weekName" placeholder="e.g., 研究, 就活, バイト"/></td>
                </tr>

                <tr>
                    <td colspan="2" style="width:100%">
                        <textarea name="journal" placeholder="所感, 次週に向けての感想"/>
                    </td>
                </tr>
            </table>
            <input type="submit" name="submit" value="ジャーナルを登録"/>
        </form>
        <List class="right_side" ref="list"/>
    </div>
</template>





<style lang="scss" scoped>
.top {
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    height: calc(100vh - 120px);
    
    @media screen and (max-width: 720px) {
        flex-direction: column;
    }
}

.left_side {
    color: white;
    background: #77868C;
    width: 30vw;
    padding: 32px;
    @media screen and (max-width: 720px) {
        width: 100vw;
        box-sizing: border-box;
    }
    table {
        width: 100%;
        margin: 0 auto;
        tr {
            height: 48px;
            td {
                width: 70%;
                text-align: center;
                vertical-align: middle;
                &:first-child { width: 30% }
            }
        }
    }
    input {
        width: 100%;
        padding: 6px 8px;
        border: 0;
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
        border: 0;
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
    @media screen and (max-width: 720px) {
        width: 100vw;
    }
}
</style>