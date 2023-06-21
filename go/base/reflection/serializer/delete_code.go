package serializer

// func setValue(src FieldValue, dst reflect.Value) error {
// 	switch src.Type {
// 	case reflect.Int:
// 		dst.SetInt(int64(src.Value.Int()))
// 	case reflect.Int8:
// 		dst.SetInt(int64(src.Value.Int()))
// 	case reflect.Int16:
// 		dst.SetInt(int64(src.Value.Int()))
// 	case reflect.Int32:
// 		dst.SetInt(int64(src.Value.Int()))
// 	case reflect.Int64:
// 		dst.SetInt(int64(src.Value.Int()))
// 	case reflect.Uint:
// 		dst.SetUint(uint64(src.Value.Uint()))
// 	case reflect.Uint8:
// 		dst.SetUint(uint64(src.Value.Uint()))
// 	case reflect.Uint16:
// 		dst.SetUint(uint64(src.Value.Uint()))
// 	case reflect.Uint32:
// 		dst.SetUint(uint64(src.Value.Uint()))
// 	case reflect.Uint64:
// 		dst.SetUint(uint64(src.Value.Uint()))
// 	case reflect.Bool:
// 		dst.SetBool(src.Value.Bool())
// 	case reflect.Float32:
// 		dst.SetFloat(float64(src.Value.Float()))
// 	case reflect.Float64:
// 		dst.SetFloat(src.Value.Float())
// 	case reflect.Complex64:
// 		dst.SetComplex(complex128(src.Value.Complex()))
// 	case reflect.Complex128:
// 		dst.SetComplex(src.Value.Complex())
// 	case reflect.String:
// 		dst.SetString(src.Value.String())
// 	case reflect.Pointer:
// 		// dst.SetPointer(src.Value.UnsafePointer())
// 		dst.Set(src.Value)
// 	default:
// 		return fmt.Errorf("unhandle case type: %s", src.Type)
// 	}
// 	return nil
// }

// func GetInstanceFieldNameToValue(instance any) (map[string]FieldValue, error) {
// 	Type := reflect.TypeOf(instance)
// 	validTypeKind := goSet.NewSet(reflect.Pointer, reflect.Struct)
// 	if !validTypeKind.Contains(Type.Kind()) {
// 		return nil, errors.New("instance must be Struct or Struct Pointer")
// 	}
// 	if Type.Kind() == reflect.Pointer && Type.Elem().Kind() != reflect.Struct {
// 		return nil, errors.New("instance must be Struct or Struct Pointer")
// 	}

// 	Value := reflect.ValueOf(instance)
// 	if Type.Kind() == reflect.Pointer {
// 		Type = Type.Elem()
// 		Value = Value.Elem()
// 	}

// 	result := make(map[string]FieldValue)
// 	for i := 0; i < Value.NumField(); i++ {
// 		fieldType := Type.Field(i)
// 		fieldValue := Value.Field(i)
// 		result[fieldType.Name] = FieldValue{
// 			Type:  fieldType.Type.Kind(),
// 			Value: fieldValue,
// 		}
// 	}
// 	return result, nil
// }

// type FieldValue struct {
// 	Type  reflect.Kind
// 	Value reflect.Value
// }
