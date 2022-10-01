CC = gcc
CXX = g++

ifeq ($(OS), Windows_NT)
RM = del
EXE = build\app.exe
else
RM = rm
EXE = ./build/app
endif

FLAGS = -Iinclude
#{ADDITIONS}#
SRC = src/sourcepath
COMPILER = compiler

$(EXE): $(SRC)
	$(COMPILER) $(SRC) $(FLAGS) -o $(EXE)

test:
ifneq ($(OS), Windows_NT)
	chmod +x $(EXE)
endif
	$(EXE)

clean:
	$(RM) $(EXE)
