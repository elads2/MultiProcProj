SHELL=/bin/sh
BENCHMARK=sp
BENCHMARKU=SP

include ../config/make_improved.def

OBJS =	sp_improved.o \
	${COMMON}/c_print_results.o ${COMMON}/c_timers.o ${COMMON}/c_wtime.o

include ../sys/make.common

${PROGRAM}: config ${OBJS}
	${CLINK} ${CLINKFLAGS} -o ${PROGRAM} ${OBJS} ${C_LIB}

sp_improved.o:		sp_improved.cpp npbparams.hpp
	${CCOMPILE} sp_improved.cpp

clean:
	- rm -f *.o *~ mputil*
	- rm -f npbparams.hpp core
