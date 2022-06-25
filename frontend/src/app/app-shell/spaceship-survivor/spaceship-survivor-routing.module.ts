import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SpaceshipSurvivorComponent } from './spaceship-survivor.component';

const routes: Routes = [
  {
    path: '',
    component: SpaceshipSurvivorComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SpaceshipSurvivorRoutingModule { }
