<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link :to="{name:'home'}" class="navbar-brand">Question Time</router-link>
            <!-- <div class="collapse navbar-collapse"> -->
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <router-link :to="{name: 'home'}" class="btn btn-sm btn-success">Home</router-link>
                    </li>
                    <li class="nav-item mx-11">
                        <router-link :to="{name: 'home'}" class="btn btn-sm btn-danger">ADD QUESTION</router-link>
                    </li>
                    <li class="nav-item">
                        <a href="/accounts/logout/" class="btn btn-sm btn-outline-secondary">Logout</a>
                    </li>
                </ul>
            <!-- </div>  -->
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavBarComponent"
};
</script>

<style>
.my-navbar {
    border-bottom: 1px solid gray;
}
.button-container {
    display: flex;
    flex-direction: row;
}
.navbar-brand {
	font-weight: bold;
	font-size: 130%;
}
.navbar-brand:hover {
	color: #DC3545 !important;
}

</style>