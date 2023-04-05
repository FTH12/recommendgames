var app = getApp()
Page({
  data: {
    img_src: app.globalData.img_src,
    navData: [
      {
        id: '42',
        text: '恋爱养成'
      },
      {
        id: '43',
        text: '格斗游戏'
      },
      {
        id: '44',
        text: '飞行射击'
      },
      {
        id: '45',
        text: '模拟游戏'
      },
      {
        id: '46',
        text: '动作游戏'
      },
      {
        id: '47',
        text: '竞速游戏'
      },
      {
        id: '48',
        text: '策略游戏'
      },
      {
        id: '49',
        text: '音乐游戏'
      },
      {
        id: '50',
        text: '第一射击'
      },
      {
        id: '51',
        text: '即时战略'
      },
      {
        id: '52',
        text: '冒险游戏'
      },
      {
        id: '53',
        text: '角色扮演'
      },
      {
        id: '55',
        text: '体育游戏'
      },
      {
        id: '56',
        text: '第三射击'
      },
      {
        id: '57',
        text: '益智游戏'
      },
      {
        id: '41',
        text: '其他游戏'
      }
    ],
    currentTab: 0,
    navScrollLeft: 0,
    list : []
  },
  switchNav(event) {
    var cur = event.currentTarget.dataset.current;
    //每个tab选项宽度占1/5
    var singleNavWidth = this.data.windowWidth / 5;
    //tab选项居中                            
    this.setData({
      navScrollLeft: (cur - 2) * singleNavWidth
    })
    console.log(this.navScrollLeft)
    if (this.data.currentTab == cur) {
      return false;
    } else {
      this.setData({
        currentTab: cur
      })
    }
  },
  switchTab(event) {
    var cur = event.detail.current;
    var singleNavWidth = this.data.windowWidth / 5;
    this.setData({
      currentTab: cur,
      navScrollLeft: (cur - 2) * singleNavWidth
    });
    let that = this
    wx.request({
      url: 'http://localhost:5000/game/getGameByType/'+this.data.navData[cur].id,
      data: {},
      method: 'GET',
      success: function (res) {
        let list = res.data.games;
        if (list == undefined) {
          let toastText = '获取失败' + res.data.errMsg;
          wx.showToast({
            title: toastText,
            icon: '',
            duration: 2000
          });
        } else {
          // console.log(commentsTime))
          that.setData({
            list: list
          });
        }
      }
    })
  },
  onLoad: function () {
    // wx.getSystemInfo({
    //   success: (res) => {
    //     this.setData({
    //       pixelRatio: res.pixelRatio,
    //       windowHeight: res.windowHeight,
    //       windowWidth: res.windowWidth
    //     })
    //   },
    // })
    let that = this
    wx.request({
      url: 'http://localhost:5000/game/getGameByType/42',
      data: {},
      method: 'GET',
      success: function (res) {
        let list = res.data.games;
        console.log(res.data.games)
        if (list == undefined) {
          let toastText = '获取失败' + res.data.errMsg;
          wx.showToast({
            title: toastText,
            icon: '',
            duration: 2000
          });
        } else {
          // console.log(commentsTime))
          that.setData({
            list: list
          });
        }
      }
    })
  },
    onReady: function () {
        // 页面渲染完成
    },
    onShow: function () {
        // 页面显示
    },
    onHide: function () {
        // 页面隐藏
    },
    onUnload: function () {
        // 页面关闭
    },
})