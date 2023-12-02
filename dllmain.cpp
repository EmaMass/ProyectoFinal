// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <string>
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

extern "C" __declspec(dllexport) int wincondition(int entrada) {
    int resultado;
        __asm {
            MOV EAX, entrada
            TEST EAX, EAX
            JZ cero 
            TEST EAX, EAX
            JS cero 
            CMP EAX, 1
            JNLE cero
            JMP uno 
                cero:
            MOV EAX, 0
            MOV resultado, EAX
            JMP salida
                uno:
            MOV EAX, 1
            MOV resultado, EAX
                salida:
    }
    return resultado;
}

extern "C" __declspec(dllexport) int moverImagen(int disco, int torre) {
    int resultado;
        __asm {
            MOV EAX, disco
            CMP EAX,1
            JBE salto1
            CMP EAX,2
            JBE salto2
            CMP EAX,3
            JBE salto3
            JMP salto4
                salto1:
                MOV EAX, torre
                CMP EAX,1
                JBE torre11
                CMP EAX,2
                JBE torre21
                JMP torre31 
                    torre11:
                    MOV EAX, 100
                    MOV resultado, EAX 
                    JMP fin
                    torre21:
                    MOV EAX, 290
                    MOV resultado, EAX
                    JMP fin
                    torre31:
                    MOV EAX, 480
                    MOV resultado, EAX
                    JMP fin
                salto2:
                    MOV EAX, torre
                    CMP EAX,1
                    JBE torre12
                    CMP EAX,2
                    JBE torre22
                    JMP torre32 
                        torre12:
                        MOV EAX, 90
                        MOV resultado, EAX 
                        JMP fin
                        torre22:
                        MOV EAX, 280
                        MOV resultado, EAX
                        JMP fin
                        torre32:
                        MOV EAX, 470
                        MOV resultado, EAX
                        JMP fin
                salto3:
                    MOV EAX, torre
                    CMP EAX,1
                    JBE torre13
                    CMP EAX,2
                    JBE torre23
                    JMP torre33 
                        torre13:
                        MOV EAX, 80
                        MOV resultado, EAX 
                        JMP fin
                        torre23:
                        MOV EAX, 270
                        MOV resultado, EAX
                        JMP fin
                        torre33:
                        MOV EAX, 460
                        MOV resultado, EAX
                        JMP fin
                 salto4:
                    MOV EAX, torre
                    CMP EAX,1
                    JBE torre14
                    CMP EAX,2
                    JBE torre24
                    JMP torre34 
                        torre14:
                        MOV EAX, 70
                        MOV resultado, EAX 
                        JMP fin
                        torre24:
                        MOV EAX, 260
                        MOV resultado, EAX
                        JMP fin
                        torre34:
                        MOV EAX, 450
                        MOV resultado, EAX
                        fin:
    }
        return resultado;
}

extern "C" __declspec(dllexport) int moverVertical(int tlength) {
        int resultado;
        __asm {
            MOV EAX, tlength 
            CMP EAX, 0
            JBE salto1
            CMP EAX, 1
            JBE salto2
            CMP EAX, 2
            JBE salto3
            JMP salto4
                salto1:
                    MOV EAX, 215
                    MOV resultado, EAX
                    JMP fin
                salto2:
                    MOV EAX, 175
                    MOV resultado, EAX
                    JMP fin
                salto3:
                    MOV EAX, 140
                    MOV resultado, EAX
                    JMP fin 
                salto4:
                    MOV EAX, 100
                    MOV resultado, EAX
                fin:
        }
        return resultado;
}


