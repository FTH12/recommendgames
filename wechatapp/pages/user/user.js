// 获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    canIUseGetUserProfile: false,
    canIUseOpenData: false,
    code: null,
  },
  // 事件处理函数
  bindViewTap() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad() {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
    }
  },
  getUserProfile(e) {
    let that = this;
    wx.login({
      success: (res) => {
          that.data.code = res.code;
          console.log(that.data.code)
      },
    })
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        console.log(res)
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true,
        })
        wx.request({
            url: 'http://127.0.0.1:5000/user/login',
            method: 'post',
            data: {code: this.data.code, userInfo: res.userInfo},
            success: res => {
                this.setData({userId: res.data.id})
                app.globalData.userInfo = res.data
                console.log(app.globalData.userInfo)
            }
          })
      }
    })
  },
})
