package main

import (
	"fmt"
	"gin-demo/auth"
	"gin-demo/auth/memstore"

	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

func main() {
	// fmt.Println("Hello Gin")

	r := gin.Default()

	// cookie.Middleware(r)
	memstore.Middleware(r)

	r.POST("/login", login)
	r.GET("/user", user)
	r.GET("/logout", logout)
	r.Run(":8000")
}

type LoginReq struct {
	Username string
}

func login(c *gin.Context) {
	var req LoginReq
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(400, gin.H{
			"error": err.Error(),
		})
		return
	}

	auth.Login(c, req.Username)

	c.JSON(200, sessionValues(c))
}

func user(c *gin.Context) {
	username := auth.AuthInfo(c)
	if username == "" {
		c.JSON(401, gin.H{
			"msg": "no auth",
		})
		return
	}

	c.JSON(200, gin.H{
		"username": username,
		"session":  sessionValues(c),
	})
}

func logout(c *gin.Context) {
	username := auth.AuthInfo(c)
	if username == "" {
		c.JSON(401, sessionValues(c))
		return
	}

	auth.Logout(c, username)
	c.JSON(200, sessionValues(c))
}

func sessionValues(c *gin.Context) map[string]any {
	session := sessions.Default(c)
	var values = make(map[string]any)
	for k, v := range session.Session().Values {
		values[fmt.Sprintf("%s", k)] = v
	}

	return map[string]any{
		"values": values,
		"id":     session.Session().ID,
		"is_new": session.Session().IsNew,
		"name":   session.Session().Name(),
	}
}
