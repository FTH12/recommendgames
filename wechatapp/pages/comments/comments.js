var app = getApp()
Page({
    data: {
        gameId: undefined,
        gameTitle: '',
        evaContent: '',
        isrecommend: 1
    },
    onLoad: function (options) {
        console.log(options)
        this.setData({
            gameId: options.gameId,
            gameTitle: options.gameTitle,
            isrecommend: options.isrecommend
        });
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
    textBlur: function (e) {
        console.log(e.detail.value)
        if (e.detail && e.detail.value.length > 0) {
            if (e.detail.value.length < 12 || e.detail.value.length > 500) {
                //app.func.showToast('内容为12-500个字符','loading',1200);
            } else {
                this.setData({
                    evaContent: e.detail.value
                });
            }
        } else {
            this.setData({
                evaContent: ''
            });

        }
    },
    evaSubmit: function (eee) {
        wx.request({
            method: "post",
            header: {
                "content-type": "application/json"
            },
            url: "http://localhost:5000/comment/addComment",
            data: {
                userInfo: app.globalData.userInfo,
                content: eee.detail.value.evaContent,
                gameId: this.data.gameId,
                isrecommend: this.data.isrecommend,
            },
            success: function (res) {
                if (res.statusCode === 200) {
                    wx.showModal({
                        title: '评论成功！',
                        content: '',
                        showCancel: false,
                        success(res) {
                            if (res.confirm) {
                                wx.navigateBack({
                                    delta: 1
                                })
                            }
                        }
                    })
                } else {
                    wx.showModal({
                        title: '评论失败！',
                        content: '',
                        showCancel: false,
                        success(res) {
                            if (res.confirm) {
                                wx.navigateBack({
                                    delta: 1
                                })
                            }
                        }
                    })
                }
            }
        })

    }
})