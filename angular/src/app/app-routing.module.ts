import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule, Routes } from '@angular/router';

import { TopGeneralFeedComponent } from './components/top-general-feed/top-general-feed.component';
import { GetArgumentComponent } from './components/argument/get-argument/get-argument.component';
import { CreateArgumentComponent } from './components/argument/create-argument/create-argument.component';
import { CreateCommunityComponent } from './components/community/create-community/create-community.component';
import { GetCommunityComponent } from './components/community/get-community/get-community.component';
import { CreateUserComponent } from './components/user/create-user/create-user.component';
import { GetUserComponent } from './components/user/get-user/get-user.component';
import { CreateDebateComponent } from './components/debate/create-debate/create-debate.component';
import { GetDebateComponent } from './components/debate/get-debate/get-debate.component';
import { NotFoundComponent } from './components/not-found/not-found.component';


const appRoutes: Routes = [
  { path: 'u', component: CreateUserComponent},
  { path: 'u/:id', component: GetUserComponent},
  { path: 'd', component: CreateDebateComponent},
  { path: 'd/:id', component: GetDebateComponent},
  { path: 'a', component: CreateArgumentComponent},
  { path: 'a/:id', component: GetArgumentComponent},
  { path: 'c', component: CreateCommunityComponent},
  { path: 'c/:id', component: GetCommunityComponent},
  { path: '', component: TopGeneralFeedComponent},
  { path: '404', component: NotFoundComponent}
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(
      appRoutes,
      {enableTracing: false}
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
