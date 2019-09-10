<template>
    <div id="app">
        <NavbarComponent />
        <router-view />
    </div>
</template>
<script>
import NavbarComponent from "./components/NavBar";
export default {
    name: "App",
    components: {
        NavbarComponent
    }
};
</script>
<style>
html,
body {
    height: 100%l font-family;
}
.btn:focus {
    box-shadow: none !important;
}
</style>
