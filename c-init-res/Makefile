CC = gcc
CXX = g++

ifeq ($(OS), Windows_NT)
RM = del
EXE = build\{name}{winext}
else
RM = rm
EXE = ./build/{name}{linext}
endif

FLAGS = -Iinclude {cloptions}
SRC = src/{sourcepath}
COMPILER = {compiler}

$(EXE): $(SRC)
	$(COMPILER) $(SRC) $(FLAGS) -o $(EXE)

test:
ifneq ($(OS), Windows_NT)
	chmod +x $(EXE)
endif
	$(EXE)

clean:
	$(RM) $(EXE)
