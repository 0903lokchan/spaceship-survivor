import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LandingPageComponent } from './landing-page.component';
import { LandingPageRoutingModule } from './landing-page-routing.module';
import { GridItemComponent } from './grid-item/grid-item.component';
import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

@NgModule({
  declarations: [LandingPageComponent, GridItemComponent],
  imports: [
    CommonModule,
    WarningMessageModule,
    LandingPageRoutingModule
  ]
})
export class LandingPageModule { }
