import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./app-shell/landing-page/landing-page.module').then(module => module.LandingPageModule)
  },
  {
    path: 'spaceship-survivor',
    loadChildren: () => import('./app-shell/spaceship-survivor/spaceship-survivor.module').then(module => module.SpaceshipSurvivorModule)
  },
  {
    path: 'dice-calculator',
    loadChildren: () => import('./app-shell/dice-calculator/dice-calculator.module').then(module => module.DiceCalculatorModule)
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }

