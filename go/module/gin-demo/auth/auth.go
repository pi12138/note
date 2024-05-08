package auth

import (
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

const (
	secert  string = "secert"
	authKey string = "username"
)

// 很简陋的 login 和 logout
// 正式环境可以需要一些额外判断，例如判断用户是否重复登录

func Login(c *gin.Context, username string) error {
	session := sessions.Default(c)
	session.Set(authKey, username)
	return session.Save()
}

func Logout(c *gin.Context, username string) error {
	session := sessions.Default(c)
	session.Clear()
	return session.Save()
}

func AuthInfo(c *gin.Context) string {
	session := sessions.Default(c)
	v := session.Get(authKey)
	vv, _ := v.(string)
	return vv
}
