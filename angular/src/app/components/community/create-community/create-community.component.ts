import { Component, OnInit } from '@angular/core';
import { CommunityService } from 'src/app/services/community/community.service';
import { Community } from '../community';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-create-community',
  templateUrl: './create-community.component.html',
  styleUrls: ['./create-community.component.css']
})
export class CreateCommunityComponent implements OnInit {
  private community: Community;

  constructor(
    public service: CommunityService,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    this.createCommunity();
  }

  createCommunity() {
    this.community = new Community('graeme4', 'graeme3');
    this.service.createCommunity(this.community).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
