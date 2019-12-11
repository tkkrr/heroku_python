<script>
import Hello from "./hello"
export default {
    components: {Hello}
}
</script>



<template>
    <div>
        <header>Graphic Design Laboratory</header>
        <Hello/>
    </div>
</template>

// scoped scss
<style lang="scss" scoped>
header {
    display: flex;
    align-items: center;
    background: #E2E0E0;
    padding: 0 60px;
    font-size: 40px;
    font-family: urbane, sans-serif;
    color: #325259;
    height: 120px;
}
</style>

// global scss
<style lang="scss">

* {
    margin: 0;
    padding: 0;
    font-size: 16px;
    list-style: none;
    font-family: din-2014, toppan-bunkyu-gothic-pr6n, sans-serif;
}

</style>