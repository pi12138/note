package memstore

import (
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/memstore"
	"github.com/gin-gonic/gin"
)

const (
	secert      string = "secert"
	sessionName string = "sessionId"
)

func Middleware(e *gin.Engine) {
	store := memstore.NewStore([]byte(secert))
	e.Use(sessions.Sessions(sessionName, store))
}
