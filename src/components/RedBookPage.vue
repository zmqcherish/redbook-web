<template>
	<!-- <div class="row my-4"> -->

	<div class="d-flex flex-row my-4">
		<!-- TODO 收藏需要做登录后才可查看 -->
		<!-- <div>
			<ul class="nav nav-pills" id="ex1" role="tablist">
				<li class="nav-item" role="presentation">
					<a class="nav-link active" id="ex1-tab-1" data-mdb-toggle="pill" href="#ex1-pills-1" role="tab"
						aria-controls="ex1-pills-1" aria-selected="true">我的</a>
				</li>
				<li class="nav-item" role="presentation">
					<a class="nav-link" id="ex1-tab-2" data-mdb-toggle="pill" href="#ex1-pills-2" role="tab"
						aria-controls="ex1-pills-2" aria-selected="false">收藏</a>
				</li>
			</ul>
		</div> -->
		<div>
			<div class="input-group">
				<div class="form-outline">
					<input class="my-form-control" v-model="queryData.searchKey" @keyup.enter="searchImage" />
				</div>
				<button type="button" class="btn btn-primary" @click="searchImage">
					<i class="fas fa-search"></i>
				</button>
			</div>
		</div>
	</div>

	<!-- </div> -->
	<Waterfall :list="rbItems" :breakpoints="breakpoints">
		<template #item="{ item }">
			<div class="card">
				<LazyImg :url="item.cover" @click="clickImage(item)" />
				<div class="card-body" @click="clickPage(item)" data-mdb-toggle="modal" data-mdb-target="#exampleModal">
					<div class="card-title">
						{{ item.display_title }}</div>
				</div>
			</div>
		</template>
	</Waterfall>
	<a v-if="hasMore" class="btn text-white mt-2" style="background-color: #55acee;" role="button" @click="pageChange">
		更多
	</a>
	<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-dialog-scrollable" style="text-align: left;">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="exampleModalLabel">{{ selectedContent.title }}</h5>
					<button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
				</div>
				
				<div class="modal-body" style="white-space: pre-wrap;">{{ selectedContent.detail }}</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-mdb-dismiss="modal">Close</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		LazyImg,
		Waterfall
	} from "vue-waterfall-plugin-next";
	import "vue-waterfall-plugin-next/style.css";
	export default {
		components: {
			LazyImg,
			Waterfall,
		},
		data() {
			return {
				hasMore: true,
				queryData: {
					searchKey: "",
					total: 1,
					page: 1,
					size: 20,
					totalPage: 1,
				},
				rbItems: [],
				breakpoints: {
					2000: {
						rowPerView: 5,
					},
					1600: {
						rowPerView: 4,
					},
					1200: {
						rowPerView: 3,
					},
					400: {
						//当屏幕宽度小于等于400
						rowPerView: 2,
					},
				},
				contentModalVisible: true,
				selectedContent: {},
			};
		},
		methods: {
			getImages() {
				let s = this.queryData.searchKey;
				let skip = (this.queryData.page - 1) * this.queryData.size;

				var cql = "select count(*),* from RedBookItem ";
				if (s != "") {
					cql += `where display_title like '%${s}%' `;
				}
				cql += `limit ${skip}, ${this.queryData.size} order by -id`;
				this.$AV.Query.doCloudQuery(cql).then((res) => {
					res.results.forEach((item) => {
						let attr = item.attributes;
						attr.cover = attr.images_list[0].url;
						let imgUrls = [];
						attr.images_list.forEach(img => {
							imgUrls.push(img.url_size_large);
						});
						attr.imgUrls = imgUrls;
						this.rbItems.push(attr);
					});
					this.queryData.total = res.count;
					this.hasMore = this.rbItems.length !== res.count;
				});
			},
			clickPage(page) {
				if (page.has_detail) {
					this.contentModalVisible = true;
					page.detail = page.detail.replaceAll("[话题]#", "");
					this.selectedContent = page;
				} else {
					window.open(
						"https://www.xiaohongshu.com/discovery/item/" + page.id,
						"_blank"
					);
				}
			},
			clickImage(item) {
				if (item.type == 'video') {
					window.open(
						"https://www.xiaohongshu.com/discovery/item/" + item.id,
						"_blank"
					);
					return;
				}
				this.$viewerApi({
					images: item.imgUrls,
					options: {
						toolbar: true,
						initialViewIndex: 0,
					},
				});
			},
			pageChange(page) {
				this.queryData.page = this.queryData.page + 1;
				this.getImages();
				// window.scrollTo(0, 0);
			},
			searchImage() {
				this.rbItems = [];
				this.queryData.page = 1;
				this.getImages();
			},
		},
		created() {
			if (this.rbItems.length == 0) {
				this.getImages();
			}
		},
	};
</script>

<style scoped>
	.my-form-control {
		/* pointer-events: none; */
		min-height: auto;
		padding: 0.33em 0.75em;
		border: 1px solid #bdbdbd;
		box-sizing: border-box;
		border-radius: 0.3;
		background: transparent;
		transition: all 0.2s linear;
	}
</style>