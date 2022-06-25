import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DiceCalculatorComponent } from './dice-calculator.component';
import { DiceCalculatorRoutingModule } from './dice-calculator-routing.module';


@NgModule({
  declarations: [DiceCalculatorComponent],
  imports: [
    CommonModule,
    DiceCalculatorRoutingModule
  ]
})
export class DiceCalculatorModule { }
