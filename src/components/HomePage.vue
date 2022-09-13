<template>
	<div class="mx-5">
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			<div class="container-fluid">
				<a
					class="navbar-brand"
					href="#"
				>CHERISH</a>
				<button
					class="navbar-toggler"
					type="button"
					data-mdb-toggle="collapse"
					data-mdb-target="#navbarNavAltMarkup"
					aria-controls="navbarNavAltMarkup"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<i class="fas fa-bars"></i>
				</button>
				<div
					class="collapse navbar-collapse"
					id="navbarNavAltMarkup"
				>
					<div class="navbar-nav">
						<!-- <router-link
							class="nav-link"
							:class="isActive('image')"
							to="/image"
							@click="onMenuSelect('image')"
						>RAW.cn</router-link>
						<router-link
							class="nav-link"
							to="/avogado6"
							:class="isActive('avogado6')"
							@click="onMenuSelect('avogado6')"
						>Avogado6</router-link> -->
						<router-link
							class="nav-link"
							to="/redbook"
							:class="isActive('redbook')"
							@click="onMenuSelect('redbook')"
						>redbook</router-link>
					</div>
				</div>
			</div>
		</nav>

		<router-view />
		<FooterPage />
	</div>
</template>

<script>
import FooterPage from "./FooterPage.vue";

export default {
	name: "HomePage",
	components: {
		FooterPage,
	},
	data() {
		return {
			avtivePath: '',
		};
	},
	methods: {
		onMenuSelect(path) {
			this.avtivePath = path;
		},
		isActive(path) {
			return this.avtivePath === path ? 'active' : '';
		},
	},
	created() {
		if(!this.avtivePath) {
			this.avtivePath = this.$route.path.replace('/', '');
		}
	}
};
</script>