INCLUDES = -I. -I../tolua++/include 
LDFLAGES = -L. -L../lua-5.1.4/src -L../tolua++/lib 


all : run

run : main.cpp student.cpp lua_student.cpp
	g++ -o run main.cpp student.cpp lua_student.cpp $(LDFLAGES) $(INCLUDES) -ldl -llua -ltolua++ 

lua_student.cpp : student.pkg 
	./tolua++ -o lua_student.cpp student.pkg  

.PHONY : clean
clean:
	rm -rf lua_student.cpp
