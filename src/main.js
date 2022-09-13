import { createApp } from 'vue'
import App from './App.vue'
import api from './api.js'

import 'viewerjs/dist/viewer.css'
import VueViewer from 'v-viewer'
import * as mdb from 'mdb-ui-kit';

import router from './router'

let AV = require('leancloud-storage');
AV.init({
	serverURLs: '你的服务器地址',
	appId: '你的appId',
	appKey: '你的appKey'
});

const app = createApp(App)
app.config.globalProperties.$api = api;
app.config.globalProperties.$AV = AV;

//options: https://www.jianshu.com/p/1fd3b4e6911c
app.use(VueViewer, { defaultOptions: {
	toolbar: false,
	navbar: false,
	movable: false,
	loop: false,
	scalable: false,	// 是否可以翻转图片
	fullscreen: false,	// 播放时是否全屏
	rotatable: false,	// 是否可以旋转图片
}})
app.use(router)

app.mount('#app')
