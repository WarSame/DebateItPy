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
  private route: ActivatedRoute;
  private service: CommunityService;
  private community: Community;
  private router: Router;

  constructor(
    route: ActivatedRoute,
    service: CommunityService,
    router: Router
    ) {
      this.service = service;
      this.route = route;
      this.community = new Community('', '');
      this.router = router;
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
