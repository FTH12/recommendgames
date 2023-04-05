//app.js
App({
  onLaunch: function (e) {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
  },
  globalData: {
    userInfo: null,
    img_src: 'http://rmh.tpddns.cn:8004/gameimg/',
  }
})