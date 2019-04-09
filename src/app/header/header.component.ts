import { Component, OnInit } from '@angular/core';
import { PageViewService } from '../core/services/page-view.service';
import { AuthService } from '../core/services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private pageViewService: PageViewService,
    private authService: AuthService
  ) {
  }

  ngOnInit() {
  }

}
