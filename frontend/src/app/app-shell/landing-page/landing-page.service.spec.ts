import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { LandingPageService } from './landing-page.service';

describe('LandingPageService', () => {
  beforeEach(async () => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    }).compileComponents();
  });

  it('should be created', () => {
    const service: LandingPageService = TestBed.inject(LandingPageService);
    expect(service).toBeTruthy();
  });
});
