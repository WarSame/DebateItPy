import { Component, OnInit } from '@angular/core';
import { TopFeedService } from '../../services/top-feed/top-feed.service';

@Component({
  selector: 'app-top-general-feed',
  templateUrl: './top-general-feed.component.html',
  styleUrls: ['./top-general-feed.component.css']
})
export class TopGeneralFeedComponent implements OnInit {
  top_debates = this.getTopGeneralFeed();

  constructor(public topFeedService: TopFeedService) {
    this.topFeedService = topFeedService;
  }

  ngOnInit() {
  }

  getTopGeneralFeed() {
    this.topFeedService.getTopDebates(5).subscribe(
      data => {
        console.log('Success retrieving top feed ');
        console.log(data);
        this.top_debates = data;
      },
      error => {
        console.log('Error ');
        console.log(error);
      }
    );
  }

  getTopTargetedFeed() {

  }

}
