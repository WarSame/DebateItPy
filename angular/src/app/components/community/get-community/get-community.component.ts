import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { CommunityService } from 'src/app/services/community/community.service';
import { Community } from '../community';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-get-community',
  templateUrl: './get-community.component.html',
  styleUrls: ['./get-community.component.css']
})
export class GetCommunityComponent implements OnInit {
  private community: Community;

  constructor(
    private route: ActivatedRoute,
    private service: CommunityService,
    private router: Router
    ) {
      this.community = new Community('', '');
     }

  ngOnInit() {
    this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getCommunity(params.get('id'))
      )
    )
    .subscribe(
      community => {
        this.community = community;
        console.log(community);
      },
      error => {
        console.log(error);
        this.router.navigate(['404']);
      });
  }

}
