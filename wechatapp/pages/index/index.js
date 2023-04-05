//获取应用实例
const app = getApp()
Page({
    data: {
        banner: [
            {
                // link : '../pages/index/',
                url: 'https://img.3dmgame.com/uploads/images/news/20190331/1553995378_886178.jpg',
            },
            {
                // link : '../pages/index',
                url: 'https://img.3dmgame.com/uploads/images/news/20190331/1553995378_886178.jpg',
            },
            {
                // link : '../pages/index',
                url: 'https://img.3dmgame.com/uploads/images/news/20190331/1553995378_886178.jpg',
            },
        ],
        channel: [],
        navbar: ['最热游戏', '最新游戏', '评分最高'],
        currentTab: 0,
        list: [],
        img_src: app.globalData.img_src,
    },
    navbarTap: function (e) {
        this.setData({
            currentTab: e.currentTarget.dataset.idx
        })
        // console.log(e.currentTarget.dataset.idx)
        if (e.currentTarget.dataset.idx == 0) {
            let that = this;
            wx.request({
                url: 'http://127.0.0.1:5000/game/initGameInfo',
                method: 'GET',
                data: {},
                success: function (res) {
                    let list = res.data.data;
                    if (list == null) {
                        let toastText = '获取数据失败' + res.data.errMsg;
                        wx.showToast({
                            title: toastText,
                            icon: '',
                            duration: 2000
                        })
                    } else {
                        that.setData({
                            list: list
                        });
                    }

                }
            })
        } else if (e.currentTarget.dataset.idx == 1) {
            let that = this;
            wx.request({
                url: 'http://localhost:5000/game/newGameInfo',
                method: 'GET',
                data: {},
                success: function (res) {
                    let list = res.data.data;
                    if (list == null) {
                        let toastText = '获取数据失败' + res.data.errMsg;
                        wx.showToast({
                            title: toastText,
                            icon: '',
                            duration: 2000
                        })
                    } else {
                        that.setData({
                            list: list
                        });
                    }
                }
            })
        } else if (e.currentTarget.dataset.idx == 2) {
            let that = this;
            wx.request({
                url: 'http://localhost:5000/game/goodGameInfo',
                method: 'GET',
                data: {},
                success: function (res) {
                    let list = res.data.data;
                    if (list == null) {
                        let toastText = '获取数据失败' + res.data.errMsg;
                        wx.showToast({
                            title: toastText,
                            icon: '',
                            duration: 2000
                        })
                    } else {
                        that.setData({
                            list: list
                        });
                    }
                }
            })
        }
    },
    onShareAppMessage: function () {
        return {
            title: 'JumpJump',
            desc: 'Jump游戏推荐',
            path: '/pages/index/index'
        }
    },


    onLoad: function () {
        let that = this;
        wx.request({
            url: 'http://127.0.0.1:5000/game/initGameInfo',
            method: 'GET',
            data: {},
            success: function (res) {
                let list = res.data.data;
                if (list == null) {
                    let toastText = '获取数据失败' + res.data.errMsg;
                    wx.showToast({
                        title: toastText,
                        icon: '',
                        duration: 2000
                    })
                } else {
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
        // console.log(this.currentTab)
    },
    onHide: function () {
        // 页面隐藏
    },
    onUnload: function () {
        // 页面关闭
    },
})
