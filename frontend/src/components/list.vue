<script>
export default {
    data() {
        return {
            journals: []
        }
    },
    created() {
        this.getList()
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
        }
    }
}
</script>




<template>
    <table border="0">
        <tr>
            <td colspan="4" class="header">最近のジャーナル作成</td>
        </tr>
        <tr v-for="item in journals" :key="item._id">
            <td class="create_date">{{ item.create_date }}</td>
            <td class="name">{{ item.name }}</td>
            <td class="journal"><p>{{ item.journal }}</p></td>
            <td class="download"><a v-bind:href="'/api/create/' + item._id">
                Download PDF
            </a></td>
        </tr>
    </table>
</template>



<style lang="scss" scoped>
.header {
    padding-left: 0;
    padding-bottom: 16px;
    font-size: 20px;
    font-weight: 600;
}

tr:nth-child(2n) {
    background: #E2E0E0;
}

table, tr, td {
    border: none;
    -webkit-border-horizontal-spacing: 0;
    -webkit-border-vertical-spacing: 0;
}

table {
    margin: 16px auto;
}

tr, td {
    height: 2.4em;
}

td {
    &:first-child {
        border-left:solid 10px silver;
    }
    padding: 0 8px;
}

td.header:first-child {
    border-left: none;
}

.journal {
    display: flex;
    align-items: center;
    p {
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        width: 360px;
        line-height: 1.2;
    }
}
</style>