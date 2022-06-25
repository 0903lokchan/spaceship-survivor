import { Component, OnInit } from '@angular/core';

import { LandingPageService } from './landing-page.service';
import { ILandingPageItem } from './landing-page.model';
import {catchError, map} from 'rxjs/operators';
import {Observable, of} from 'rxjs';

@Component({
  selector: 'app-grid',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {
  greyBoxUrl = '../../../assets/GreyBox.svg';
  warningMessageText = '';
  warningMessageOpen = false;
  gridItems$: Observable<ILandingPageItem[]>;

  constructor(private gridService: LandingPageService) {}

  ngOnInit(): void {
    this.gridItems$ = this.gridService.getGridItems().pipe(catchError((error) => {
      this.warningMessageText =  `Request to get grid text failed: ${error}`;
      this.warningMessageOpen = true;
      return of(null);
    }));
  }

  handleWarningClose(open: boolean): void {
    this.warningMessageOpen = open;
    this.warningMessageText = '';
  }
}
