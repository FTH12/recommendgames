var app = getApp()
Page({
  data: {
    keyword: '',
    searchStatus: false,
    helpKeyword: [],
    historyKeyword: [],
    categoryFilter: false,
    currentSortType: 'default',
    currentSortOrder: '',
    filterCategory: [],
    defaultKeyword: {},
    hotKeyword: [],
    currentSortType: 'id',
    currentSortOrder: 'desc',
    categoryId: 0,
    img_src: app.globalData.img_src,
  },
  //事件处理函数
  closeSearch: function () {
    wx.navigateBack()
  },
  clearKeyword: function () {
    this.setData({
      keyword: '',
      searchStatus: false
    });
  },
  onLoad: function () {
  },

  inputChange: function (e) {
    this.setData({
      keyword: e.detail.value,
      searchStatus: false
    });
  },
  inputFocus: function () {
    this.setData({
      searchStatus: false,
      goodsList: []
    });

    // if (this.data.keyword) {
    //   this.getHelpKeyword();
    // }
  },
  clearHistory: function () {
    this.setData({
      historyKeyword: []
    })
  },
  onKeywordTap: function (event) {

    this.getSearchResult(event.target.dataset.keyword);

  },
  getSearchResult(keyword) {
    this.setData({
      keyword: keyword,
      page: 1,
      categoryId: 0,
      goodsList: []
    });
    this.getGoodsList();
  },
  onKeywordConfirm(event) {
    this.getSearchResult(event.detail.value);
  },
  getGoodsList() {
    var keyword = this.data.keyword;
    let that = this;
    console.log(keyword)
    wx.request({
      url: 'http://127.0.0.1:5000/game/getGamesByName/'+keyword,
      method: 'GET',
      data: {},
      success: function(res){
        let list = res.data.games;
        console.log(list)
        if(list == null){
          let toastText = '获取数据失败';
          wx.showToast({
            title: toastText,
            icon: '',
            duration: 2000
          })
        }else{
          that.setData({
            list: list
          })
        }
      }
    })
  },
})