#include <avr/io.h>

int main(void)
{

    DDRB = 0x08;                         // Setup PB3 as output

    TCCR0 |= (1<<WGM00)|(1<<WGM01)       // Start timer0 without
             |(1<<COM01)|(1<<CS00);      // prescaler in non
                                         // inverting fast PWM
                                         // mode. Connect OC0 in
                                         // non-inverting mode

    OCR0 = 64;                           // Set Dutycycle to 25%

    for(;;);                             // Endless loop
                                         // main() will never be left

    return 0;                            // This line will never be executed

}