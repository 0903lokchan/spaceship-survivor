import { Component, OnInit, Input } from '@angular/core';
import { ILandingPageItem } from '../landing-page.model';

@Component({
  selector: 'app-grid-item',
  templateUrl: './grid-item.component.html',
  styleUrls: ['./grid-item.component.css']
})
export class GridItemComponent implements OnInit {
  @Input() key: number;
  @Input() gridItem: ILandingPageItem;

  constructor() {}

  ngOnInit(): void {}
}
