import { Component, OnInit } from '@angular/core';
import { switchMap } from 'rxjs/operators';
import { ParamMap, ActivatedRoute, Router } from '@angular/router';
import { UserService } from 'src/app/services/user/user.service';
import { User } from '../user';

@Component({
  selector: 'app-get-user',
  templateUrl: './get-user.component.html',
  styleUrls: ['./get-user.component.css']
})
export class GetUserComponent implements OnInit {
  private user: User;

  constructor(
    private route: ActivatedRoute,
    private service: UserService,
    private router: Router
  ) {
    this.user = new User('', '');
  }

  ngOnInit() {
    this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getUser(params.get('id'))
      )
    )
    .subscribe(
      user => {
        this.user = user;
        console.log(user);
      },
      error => {
        console.log(error);
        this.router.navigate(['404']);
      });
  }

}
