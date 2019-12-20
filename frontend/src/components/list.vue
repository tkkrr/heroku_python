<script>
export default {
    data() {
        return {
            journals: [],
            isSmartphone: false,
        }
    },
    created() {
        this.getList()
        if ( window.innerWidth < 720 ) {
            this.isSmartphone = true
        }

    },
    methods: { 
        getList() {
            const url = '/api/recent'
            fetch( url )
                .then( response => response.json() )
                .then( json => {     
                    this.journals = json.entlies
                }) 
                .catch( error => console.error(error) )
        },
        handleClickDelete(id) {
            fetch( '/api/delete/' + id , {method: 'DELETE'})
                .then( response => response.json() )
                .then( json => console.log(json))
                .catch( error => console.log(error) )
            this.getList()
        }
    }
}
</script>




<template>
    <div class="top">
        <table v-if="journals.length != 0">
            <thead>
                <tr>
                    <td colspan="4" class="header">最新のジャーナル</td>
                </tr>
                <tr>
                    <td>作成日</td>
                    <td>作成者</td>
                    <td v-if="isSmartphone == false">概要</td>
                    <td></td>
                    <td></td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in journals" :key="item._id">
                    <td class="create_date">{{ item.create_date }}</td>
                    <td class="name">{{ item.name }}</td>
                    <td v-if="isSmartphone == false" class="journal"><p>{{ item.journal }}</p></td>
                    <td v-if="isSmartphone == false" class="download"><a v-bind:href="'/api/create/' + item._id">
                        Download PDF
                    </a></td>
                    <td v-else class="download"><a v-bind:href="'/api/create/' + item._id">
                        DL
                    </a></td>
                    <td v-if="isSmartphone == false" class="delete"><a @click="handleClickDelete(item._id)">delete</a></td>
                    <td v-else class="delete"><a @click="handleClickDelete(item._id)">削除</a></td>
                </tr>
            </tbody>
        </table>
        <h1 v-else>
            最近の投稿はありません
        </h1>
    </div>
</template>



<style lang="scss" scoped>
div .top {
    width: auto;
    margin: 0 16px;
}

.header {
    padding-left: 0;
    padding-bottom: 16px;
    font-size: 20px;
    font-weight: 600;
}

h1 {
    margin: 24px 16px; 
}

tr:nth-child(2n) {
    background: #E2E0E0;
}

table, tr, td {
    border: 0;
    outline: none;
}

table {
    width: calc( 100% - 10px );
    margin: 16px auto;
}

thead tr {
    box-sizing: border-box;
    td {
        padding: 12px 16px;
        vertical-align:middle;
        &:first-child {
            border-left: solid 10px transparent;
        }
    }
    &:last-child {
        font-weight: 900;
        background: grey;
        color: white;
    }
}

tbody tr {
    box-sizing: border-box;
    td {
        position: relative;
        vertical-align: middle;
        padding: 12px 16px;
        &:first-child::before {
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            display: block;
            border-left: 10px solid silver;
        }
    }
}

.journal {
    p {
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        width: 360px;
        line-height: 1.2;
        @media screen and (max-width: 720px) {
            width: auto;
        }
    }
}
</style>