package serializer

type UserSerializer struct {
	Name string `mser:"source:Name"`
}
