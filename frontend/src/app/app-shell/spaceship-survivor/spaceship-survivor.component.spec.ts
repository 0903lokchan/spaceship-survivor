import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpaceshipSurvivorComponent } from './spaceship-survivor.component';

describe('SpaceshipSurvivorComponent', () => {
  let component: SpaceshipSurvivorComponent;
  let fixture: ComponentFixture<SpaceshipSurvivorComponent>;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [SpaceshipSurvivorComponent]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SpaceshipSurvivorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
