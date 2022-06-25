import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { DiceCalculatorModule } from './app-shell/dice-calculator/dice-calculator.module';
import { SpaceshipSurvivorModule } from './app-shell/spaceship-survivor/spaceship-survivor.module';
import { LandingPageModule } from './app-shell/landing-page/landing-page.module';
import { NavBarComponent } from './app-shell/nav-bar/nav-bar.component';
import { FooterComponent } from './app-shell/footer/footer.component';
import { ServiceInterceptor } from './service.interceptor';

@NgModule({
  declarations: [AppComponent, NavBarComponent, FooterComponent],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    DiceCalculatorModule,
    SpaceshipSurvivorModule,
    LandingPageModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: ServiceInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
