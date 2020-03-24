def show_args(arg1, arg2, arg3="THree"):
	print(arg1, arg2, arg3)

args = range(3)
more_args = {
	"arg1": "ONE",
	"arg2": "TWO"
}

print("Unpacking a sequence: ", end="")
show_args(*args)

print("Unpacking a dict: ", end="")
show_args(**more_args)