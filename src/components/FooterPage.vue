<template>
	<footer class="text-center text-lg-start bg-white text-muted">
		<section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
			<div class="me-5 d-none d-lg-block">
				<span>星联CSVA星空摄影师｜RAW.cn供稿人｜视觉中国签约摄影师｜猫の爱好者｜故宫爱好者｜UESTC｜程序员｜@甄星cherish</span>
			</div>
			<div>
				<a class="btn text-white btn-floating m-1" style="background-color: #14A44D;" role="button"
					data-mdb-toggle="modal" data-mdb-target="#wxModal"><i class="fab fa-weixin"></i></a>
				<a class="btn text-white btn-floating m-1" style="background-color: #dd4b39;"
					href="https://weibo.com/zmqcherish" role="button" target="_blank"><i class="fab fa-weibo"></i></a>
				<a class="btn text-white btn-floating m-1" style="background-color: #ac2bac;" role="button"
					data-mdb-toggle="modal" data-mdb-target="#rbModal"><i class="fas fa-atlas"></i></a>
				<a class="btn text-white btn-floating m-1" style="background-color: #55acee;"
					href="mailto:zmqcherish@outlook.com" role="button"><i class="far fa-envelope"></i>
					></a>
				<a class="btn text-white btn-floating m-1" style="background-color: #333333;"
					href="https://github.com/zmqcherish" role="button" target="_blank"><i class="fab fa-github"></i></a>
			</div>
		</section>
		<div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.025);">
			© 2022 Copyright | created by <a class="text-reset fw-bold" href="https://cn.vuejs.org/">Vue.js</a> & <a
				class="text-reset fw-bold" href="https://mdbootstrap.com/">MDBootstrap</a>
			<a class="text-reset fw-bold" href=""></a>
		</div>
	</footer>

	<div class="modal fade" id="wxModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal modal-dialog-centered">
			<div class="modal-body"><img :src="wxImg" style="width: 100%" /></div>
		</div>
	</div>

	<div class="modal fade" id="rbModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal modal-dialog-centered">
			<div class="modal-body"><img :src="rbImg" style="width: 100%" /></div>
		</div>
	</div>

</template>
<script>
	export default {
		data() {
			return {
				wxImg: require('@/assets/wechat.jpg'),
				rbImg: require('@/assets/redbook.jpg'),
			};
		}
	}
</script>
<style>
	.my-footer {
		margin-bottom: 0;
	}
</style>