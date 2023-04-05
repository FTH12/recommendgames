const util = require('../../utils/util.js')

var app = getApp()
Page({
    data: {
        navbar: ['游戏信息', '评测'],
        currentTab: 0,
        gameId: undefined,
        gameTitle: '',
        list: [],
        listPosting: [],
        gameCommunityImage: "",
        gameCommunityId: undefined,
        img_src: app.globalData.img_src,
        ishas: 0,
        islike: 0,
        userId: (app.globalData.userInfo==null?'':app.globalData.userInfo.id),
        comment_count: 0,
    },
    navbarTap: function (e) {
        this.setData({
            currentTab: e.currentTarget.dataset.idx
        })
        if (e.currentTarget.dataset.idx == 0) {
        } else if (e.currentTarget.dataset.idx == 1) {
            let that = this
            wx.request({
                url: 'http://localhost:5000/comment/getCommentByGameId/'+this.data.gameId,
                data: {},
                method: 'GET',
                success: function (res) {
                    console.log(res)
                    let list = res.data.data;
                    let comment_count = res.data.count;
                    if (list == undefined) {
                        let toastText = '获取失败' + res.data.errMsg;
                        wx.showToast({
                            title: toastText,
                            icon: '',
                            duration: 2000
                        });
                    } else {
                        that.setData({
                            list: list,
                            comment_count: comment_count
                        });
                    }
                }
            })
        }
    },
    onLoad: function (options) {
        let that = this;
        this.setData({
            gameId: options.gameId
        });
        // console.log(this.data.gameId)
        wx.request({
            url: 'http://localhost:5000/game/getGameById/' + options.gameId,
            data: {},
            method: 'GET',
            success: function (res) {
                let game = res.data;
                // console.log(game)
                if (game == undefined) {
                    let toastText = '获取失败';
                    wx.showToast({
                        title: toastText,
                        icon: '',
                        duration: 2000
                    });
                } else {
                    that.setData({
                        gameTitle: game.name,
                        gamePublishTime: game.ss_time,
                        gamePublisherName: game.company,
                        gameTypeName: game.it_type,
                        // gameContent: game.gameContent,
                        gameScore: game.score,
                        gameImage: game.img_name,
                        gameYear: game.year,
                        gameTags: game.gtags,
                        gamePlatforms: game.platforms,
                        gameIntroduce: game.jj,
                    });
                }
            }
        })
    },
    onReady: function () {
        // 页面渲染完成
        console.log(app.globalData.userInfo)
        console.log(this.data.gameId)
        if (app.globalData.userInfo !== null) {
            this.setData({ userId: app.globalData.userInfo.id })
            wx.request({
                url: 'http://localhost:5000/user/ishasgame/' + this.data.userId + '/' + this.data.gameId,
                method: 'GET',
                data: {},
                success: res => {
                    this.setData({ ishas: res.data.ishas })
                    this.setData({ islike: res.data.islike })
                }
            })
        }
    },
    onShow: function (options) {
        // 页面显示
    },
    onHide: function () {
        // 页面隐藏
    },
    onUnload: function () {
        // 页面关闭
    },
    recommend: function (options) {
        console.log(this.data.gameId)
        if (app.globalData.userInfo!==null) {
            wx.navigateTo({
                url: '/pages/comments/comments?gameTitle=' + this.data.gameTitle + '&isrecommend=1&gameId='+this.data.gameId,
            })
        } else {
            wx.showModal({
                title: '未登录！',
                content: '请登录后再试',
            })
        }
    },
    norecommend: function (options) {
        if (app.globalData.userInfo!==null) {
            wx.navigateTo({
                url: '/pages/comments/comments?gameTitle=' + this.data.gameTitle + '&isrecommend=-1&gameId='+this.data.gameId,
            })
        } else {
            wx.showToast({
                title: '未登录，请登录后再试',
            })
        }
    },
    addPosting: function (options) {
        wx.navigateTo({
            url: '/pages/addPosting/addPosting?gameId=' + this.data.gameId + '&gameCommunityId=' + this.data.gameCommunityId,
        })
    },
    haveit: function (e) {
        if (app.globalData.userInfo == null) {
            let toastText = '请先登录';
            wx.showToast({
                title: toastText,
                icon: 'error',
                duration: 2000
            });
            return
        }
        if (this.data.ishas == 0) {
            wx.request({
                url: 'http://localhost:5000/user/havegame/' + this.data.userId + '/' + this.data.gameId,
                method: 'GET',
                success: res => {
                    if (res.statusCode === 500) {
                        wx.showToast({
                            title: '加入失败',
                            icon: 'error',
                            duration: 2000
                        });
                    } else if (res.statusCode === 200) {
                        this.setData({ ishas: 1 })
                    }
                }
            })
        } else {
            wx.request({
                url: 'http://localhost:5000/user/delgamefromlibrary/' + this.data.userId + '/' + this.data.gameId,
                method: 'GET',
                success: res => {
                    if (res.statusCode === 500) {
                        wx.showToast({
                            title: '请求失败',
                            icon: 'error',
                            duration: 2000
                        });
                    } else if (res.statusCode === 200) {
                        this.setData({ ishas: 0 })
                    }
                }
            })
        }
    },
    likeit: function (e) {
        if (app.globalData.userInfo == null) {
            let toastText = '请先登录';
            wx.showToast({
                title: toastText,
                icon: 'error',
                duration: 2000
            });
            return
        }
        if (this.data.islike == 0) {
            wx.request({
                url: 'http://localhost:5000/user/likegame/' + this.data.userId + '/' + this.data.gameId,
                method: 'GET',
                success: res => {
                    if (res.statusCode === 500) {
                        wx.showToast({
                            title: '加入失败',
                            icon: 'error',
                            duration: 2000
                        });
                    } else if (res.statusCode === 200) {
                        this.setData({ islike: 1 })
                    }
                }
            })
        } else {
            wx.request({
                url: 'http://localhost:5000/user/delgamefromlike/' + this.data.userId + '/' + this.data.gameId,
                method: 'GET',
                success: res => {
                    if (res.statusCode === 500) {
                        wx.showToast({
                            title: '请求失败',
                            icon: 'error',
                            duration: 2000
                        });
                    } else if (res.statusCode === 200) {
                        this.setData({ islike: 0 })
                    }
                }
            })
        }
    },
})