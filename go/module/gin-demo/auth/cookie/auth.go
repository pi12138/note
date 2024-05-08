package cookie

import (
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
)

const (
	secert      string = "secert"
	sessionName string = "sessionId"
)

func Middleware(e *gin.Engine) {
	store := cookie.NewStore([]byte(secert))
	e.Use(sessions.Sessions(sessionName, store))
}
