# Belajar Casting atau merubah tipe data
# tipe data = int, float, str, bool

## Data Integer
print("============INTEGER============")
data_int = 9;
print("data= ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)# akan false jika nilai int = 0
print("data= ", data_float, ",type =",type(data_float)) 
print("data= ", data_str, ",type =",type(data_str)) 
print("data= ", data_bool, ",type =",type(data_bool)) 

## Data Float
print("============FLOAT============")
data_float = 9.5;
print("data= ", data_float, ",type =",type(data_float))

data_int = int(data_float)# akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)# akan false jika nilt = 0
print("data= ", data_int, ",type =",type(data_int)) 
print("data= ", data_str, ",type =",type(data_str)) 
print("data= ", data_bool, ",type =",type(data_bool)) 

## Data String
print("============STRING============")
data_str = "10";
print("data= ", data_str, ",type =",type(data_str))

data_int = int(data_str)# akan dibulatkan kebawah
data_float = float(data_str)
data_bool = bool(data_str)# akan false jika nilt = 0
print("data= ", data_int, ",type =",type(data_int)) 
print("data= ", data_float, ",type =",type(data_float)) 
print("data= ", data_bool, ",type =",type(data_bool)) 

## Data Boolean
print("============BOOLEAN============")
data_bool = True;
print("data= ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool)# string harus angka
data_str = str(data_bool)#string harus angka
data_float = float(data_bool)# akan false jika string kosong
print("data= ", data_int, ",type =",type(data_int)) 
print("data= ", data_str, ",type =",type(data_str)) 
print("data= ", data_float, ",type =",type(data_float)) 