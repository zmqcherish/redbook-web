import { createWebHistory, createWebHashHistory, createRouter } from "vue-router";
import HomePage from "../components/HomePage.vue";
import RedBookPage from "../components/RedBookPage.vue";

const routes = [
	{
		path: "/:catchAll(.*)",
		component: HomePage,
	},
	{
		path: '/',
		name: 'HomePage',
		component: HomePage,
		// meta: {
		// 	title: ''
		// },
		children: [
			{
				path: 'redbook',
				component: RedBookPage,
			},
		]
	}

]

const router = createRouter({
	history: createWebHashHistory(),	//createWebHistory 模式会导致直接打开url会404 需要改nginx,
	routes,
})

export default router