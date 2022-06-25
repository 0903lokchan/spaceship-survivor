import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SpaceshipSurvivorComponent } from './spaceship-survivor.component';
import { SpaceshipSurvivorRoutingModule } from './spaceship-survivor-routing.module';


@NgModule({
  declarations: [SpaceshipSurvivorComponent],
  imports: [
    CommonModule,
    SpaceshipSurvivorRoutingModule
  ]
})
export class SpaceshipSurvivorModule { }
