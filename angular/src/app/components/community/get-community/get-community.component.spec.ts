import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GetCommunityComponent } from './get-community.component';

describe('GetCommunityComponent', () => {
  let component: GetCommunityComponent;
  let fixture: ComponentFixture<GetCommunityComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GetCommunityComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GetCommunityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
