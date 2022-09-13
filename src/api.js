let AV = require('leancloud-storage');

const api = {
	GET_PICTURE: () => {
		let query = new AV.Query('Pic');
		query.addAscending('id');
		return query.limit(999).find();
	},
}

export default api