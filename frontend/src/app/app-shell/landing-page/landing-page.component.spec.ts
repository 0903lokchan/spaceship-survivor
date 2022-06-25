import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { LandingPageComponent } from './landing-page.component';
import { GridItemComponent } from './grid-item/grid-item.component';
import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

describe('LandingPageComponent', () => {
  let component: LandingPageComponent;
  let fixture: ComponentFixture<LandingPageComponent>;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [LandingPageComponent, GridItemComponent],
      imports: [WarningMessageModule, HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LandingPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
